export async function getContainers() {
  const res = await fetch("http://localhost:8000/contenedores");
  if (!res.ok) throw new Error("Error al obtener contenedores");
  return res.json();
}