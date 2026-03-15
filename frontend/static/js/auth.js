const API_BASE = "http://localhost:5000/api/auth";

const loginForm = document.getElementById("loginForm");
const registerForm = document.getElementById("registerForm");
const errorMsg = document.getElementById("errorMsg");

// Tabs
document.getElementById("loginTab").addEventListener("click", () => {
    loginForm.style.display = "block";
    registerForm.style.display = "none";
    errorMsg.textContent = "";
});

document.getElementById("registerTab").addEventListener("click", () => {
    loginForm.style.display = "none";
    registerForm.style.display = "block";
    errorMsg.textContent = "";
});

// Login
loginForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const email = document.getElementById("loginEmail").value;

    try {
        const res = await fetch(`${API_BASE}/login`, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({email})
        });
        if (!res.ok) throw new Error("Invalid login");
        const data = await res.json();
        sessionStorage.setItem("token", data.access_token);
        sessionStorage.setItem("user", data.email);
        window.location.href = "/dashboard";
    } catch (err) {
        errorMsg.textContent = err.message;
    }
});

// Register
registerForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const email = document.getElementById("regEmail").value;
    const first_name = document.getElementById("regFirst").value;
    const last_name = document.getElementById("regLast").value;
    const password = document.getElementById("regPassword").value;

    try {
        const res = await fetch(`${API_BASE}/register`, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({email, first_name, last_name, password})
        });
        if (!res.ok) throw new Error("Registration failed");
        const data = await res.json();
        sessionStorage.setItem("token", data.access_token);
        sessionStorage.setItem("user", data.email);
        window.location.href = "/dashboard";
    } catch (err) {
        errorMsg.textContent = err.message;
    }
});