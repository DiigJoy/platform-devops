"use client";

import { useMemo, useState } from "react";

type Health = { status: string; db: string };
const API_BASE = process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000";

export default function Home() {
  const [health, setHealth] = useState<Health | null>(null);
  const [latencyMs, setLatencyMs] = useState<number | null>(null);
  const [error, setError] = useState<string | null>(null);

  const apiUrl = useMemo(() => `${API_BASE}/health`, []);

  async function ping() {
    setError(null);
    const t0 = performance.now();
    try {
      const res = await fetch(apiUrl, { cache: "no-store" });
      const data = (await res.json()) as Health;
      setLatencyMs(Math.round(performance.now() - t0));
      setHealth(data);
    } catch (e: any) {
      setError(e?.message ?? "Unknown error");
    }
  }

  return (
    <>
      <h1 className="headline">Pilot IoT Agricultura</h1>
      <p className="subhead">
        Vertical slice: MQTT → FastAPI → InfluxDB → Grafana. Usa el dashboard IoT
        para ver telemetria en tiempo real.
      </p>

      <div className="grid">
        <div className="card">
          <h3>Estado de la API</h3>
          <p className="subhead">Verifica salud y latencia del backend.</p>
          <button onClick={ping}>Ping API /health</button>
          <div style={{ marginTop: 12 }}>
            <small>API base:</small> <code>{API_BASE}</code>
          </div>
          {latencyMs !== null && (
            <div style={{ marginTop: 8 }}>
              <small>Latency:</small> <code>{latencyMs}ms</code>
            </div>
          )}
          {health && (
            <pre style={{ marginTop: 12 }}>{JSON.stringify(health, null, 2)}</pre>
          )}
          {error && (
            <pre style={{ marginTop: 12, color: "tomato" }}>{error}</pre>
          )}
        </div>

        <div className="card">
          <h3>Stack del piloto</h3>
          <ul>
            <li>MQTT (Mosquitto) para ingesta IoT</li>
            <li>FastAPI + InfluxDB para telemetria</li>
            <li>Grafana para dashboards</li>
            <li>Next.js para UI de demostracion</li>
          </ul>
        </div>
      </div>
    </>
  );
}
