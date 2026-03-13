document.addEventListener("DOMContentLoaded", () => {
  const searchInput = document.getElementById("tableSearch");
  if (!searchInput) return;

  const targetId = searchInput.dataset.tableTarget;
  const table = document.getElementById(targetId);
  if (!table) return;

  searchInput.addEventListener("input", () => {
    const query = searchInput.value.toLowerCase().trim();
    table.querySelectorAll("tbody tr").forEach((row) => {
      row.style.display = row.innerText.toLowerCase().includes(query) ? "" : "none";
    });
  });
});
