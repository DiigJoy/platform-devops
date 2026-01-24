import Link from "next/link";
import "./globals.css";

export const metadata = {
  title: "Platform Web",
  description: "Sprint 0 Foundation"
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="es">
      <body>
        <main>
          <nav>
            <Link className="nav-link" href="/">
              Overview
            </Link>
            <Link className="nav-link" href="/iot">
              IoT Dashboard
            </Link>
          </nav>
          {children}
        </main>
      </body>
    </html>
  );
}
