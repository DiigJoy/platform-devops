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
      <h1>🚀 Sprint 0 — Foundation</h1>
      <p>
        Web (Next.js) hablando con API (FastAPI) + Postgres, todo por Docker Compose.
      </p>

      <div className="card">
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
        <h3>Next pasos (Sprint 1)</h3>
        <ul>
          <li>Auth + tenants + users</li>
          <li>DB migrations (Alembic)</li>
          <li>ArgoCD (GitOps) + ambientes dev/stage</li>
        </ul>
      </div>
    </>
  );
}
