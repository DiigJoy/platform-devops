"use client";

import { useState } from "react";

type TelemetryPoint = {
  time: string;
  device_id: string;
  temperature_c?: number | null;
  humidity_pct?: number | null;
  soil_moisture_pct?: number | null;
};

const API_BASE = process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000";

function Sparkline({
  values,
  width = 260,
  height = 80,
}: {
  values: number[];
  width?: number;
  height?: number;
}) {
  if (values.length === 0) {
    return <div style={{ color: "#6f6a60" }}>Sin datos</div>;
  }

  const min = Math.min(...values);
  const max = Math.max(...values);
  const range = max - min || 1;
  const points = values
    .map((value, index) => {
      const x = (index / Math.max(values.length - 1, 1)) * width;
      const y = height - ((value - min) / range) * height;
      return `${x},${y}`;
    })
    .join(" ");

  return (
    <svg width={width} height={height} role="img" aria-label="sparkline">
      <polyline
        fill="none"
        stroke="#0f7a6c"
        strokeWidth="2"
        points={points}
      />
    </svg>
  );
}

export default function IoTDashboard() {
  const [deviceId, setDeviceId] = useState("sensor-001");
  const [items, setItems] = useState<TelemetryPoint[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const apiUrl = `${API_BASE}/iot/last?device_id=${encodeURIComponent(deviceId)}&limit=40`;

  async function loadData() {
    setLoading(true);
    setError(null);
    try {
      const res = await fetch(apiUrl, { cache: "no-store" });
      if (!res.ok) {
        throw new Error(`API error ${res.status}`);
      }
      const data = (await res.json()) as { items: TelemetryPoint[] };
      setItems(data.items || []);
    } catch (err: any) {
      setError(err?.message ?? "Error cargando datos");
    } finally {
      setLoading(false);
    }
  }

  const temps = items.map((item) => item.temperature_c).filter((v): v is number => typeof v === "number");
  const humidities = items.map((item) => item.humidity_pct).filter((v): v is number => typeof v === "number");
  const soil = items.map((item) => item.soil_moisture_pct).filter((v): v is number => typeof v === "number");

  const latest = items[0];

  return (
    <>
      <h1 className="headline">IoT Agriculture Dashboard</h1>
      <p className="subhead">
        Datos desde MQTT en tiempo real. Cambia el dispositivo y refresca para ver
        la telemetria.
      </p>

      <div className="card">
        <div style={{ display: "flex", gap: 12, flexWrap: "wrap", alignItems: "center" }}>
          <label>
            <small>Device ID</small>
            <div>
              <input
                value={deviceId}
                onChange={(event) => setDeviceId(event.target.value)}
                style={{
                  padding: "8px 12px",
                  borderRadius: 10,
                  border: "1px solid rgba(31, 31, 27, 0.2)",
                  marginTop: 6,
                }}
              />
            </div>
          </label>
          <button onClick={loadData} disabled={loading}>
            {loading ? "Cargando..." : "Refrescar"}
          </button>
          <button className="secondary" onClick={() => setItems([])}>
            Limpiar
          </button>
          {error && <span style={{ color: "tomato" }}>{error}</span>}
        </div>
      </div>

      <div className="grid">
        <div className="card">
          <h3>Temperatura (C)</h3>
          <Sparkline values={temps.slice().reverse()} />
          <div style={{ marginTop: 12 }}>
            <small>Ultimo valor:</small>{" "}
            <strong>{latest?.temperature_c ?? "n/a"}</strong>
          </div>
        </div>
        <div className="card">
          <h3>Humedad (%)</h3>
          <Sparkline values={humidities.slice().reverse()} />
          <div style={{ marginTop: 12 }}>
            <small>Ultimo valor:</small>{" "}
            <strong>{latest?.humidity_pct ?? "n/a"}</strong>
          </div>
        </div>
        <div className="card">
          <h3>Humedad de suelo (%)</h3>
          <Sparkline values={soil.slice().reverse()} />
          <div style={{ marginTop: 12 }}>
            <small>Ultimo valor:</small>{" "}
            <strong>{latest?.soil_moisture_pct ?? "n/a"}</strong>
          </div>
        </div>
        <div className="card">
          <h3>Ultimos eventos</h3>
          {items.length === 0 ? (
            <p className="subhead">Sin telemetria cargada.</p>
          ) : (
            <div style={{ maxHeight: 240, overflow: "auto" }}>
              <table style={{ width: "100%", borderCollapse: "collapse" }}>
                <thead>
                  <tr style={{ textAlign: "left", fontSize: 12, color: "#6f6a60" }}>
                    <th>Hora</th>
                    <th>Temp</th>
                    <th>Hum</th>
                    <th>Suelo</th>
                  </tr>
                </thead>
                <tbody>
                  {items.slice(0, 12).map((item) => (
                    <tr key={item.time}>
                      <td>{new Date(item.time).toLocaleTimeString()}</td>
                      <td>{item.temperature_c ?? "-"}</td>
                      <td>{item.humidity_pct ?? "-"}</td>
                      <td>{item.soil_moisture_pct ?? "-"}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </div>
      </div>
    </>
  );
}
