import Link from "next/link";

export default function Home() {
  return (
    <div className="container mt-5">
      <h1>Docker Dashboard Frontend</h1>
      <p>
        API lista en{" "}
        <a href="http://localhost:8000" target="_blank" rel="noopener noreferrer">
          http://localhost:8000
        </a>
      </p>

      <Link href="/contenedores">
        <button className="btn btn-primary mt-3">Ver contenedores</button>
      </Link>
    </div>
  );
}
