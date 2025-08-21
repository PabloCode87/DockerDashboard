import { useEffect, useState } from "react";
import { getContainers } from "../services/api";

interface Container {
  id: number;
  name: string;
  status: string;
  image: string;
  cpuUsage?: number;
  memoryUsage?: number;
}

export default function Containers() {
  const [containers, setContainers] = useState<Container[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getContainers()
      .then(data => setContainers(data))
      .finally(() => setLoading(false));
  }, []);

  return (
    <div className="container mt-5">
      <h2 className="mb-4">Lista de Contenedores</h2>
      {loading ? (
        <div>Cargando...</div>
      ) : (
        <div className="row">
          {containers.map(c => (
            <div key={c.id} className="col-md-4 mb-3">
              <div className="card h-100 shadow-sm">
                <div className="card-body">
                  <h5 className="card-title">{c.name}</h5>
                  <p className="card-text">
                    <strong>Status:</strong> {c.status} <br />
                    <strong>Imagen:</strong> {c.image} <br />
                    <strong>CPU:</strong> {c.cpuUsage ?? "-"} <br />
                    <strong>Memoria:</strong> {c.memoryUsage ?? "-"}
                  </p>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}