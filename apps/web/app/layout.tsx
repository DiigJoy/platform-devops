import "./globals.css";

export const metadata = {
  title: "Platform Web",
  description: "Sprint 0 Foundation"
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="es">
      <body>
        <main>{children}</main>
      </body>
    </html>
  );
}
