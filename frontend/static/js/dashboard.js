document.addEventListener("DOMContentLoaded", () => {
    loadDashboard()
})

async function loadDashboard() {
    try {
        const health = await fetch("/api/health")
        if (health.ok) {
            console.log("API connected")
        }
    } catch (error) {
        console.error("API error:", error)
    }
}
