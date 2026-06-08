async function search() {
    const industry = document.getElementById("industry").value
    const location = document.getElementById("location").value
    const interests = document.getElementById("interests").value
    const role_type = document.getElementById("role_type").value

    if (!industry || !location) {
        alert("Please enter an industry and location")
        return
    }

    document.getElementById("loading").style.display = "flex"
    document.getElementById("results").style.display = "none"

    const params = new URLSearchParams({ industry, location, interests, role_type })
    const response = await fetch(`/search?${params}`)
    const companies = await response.json()

    document.getElementById("loading").style.display = "none"
    document.getElementById("results").style.display = "block"

    const tbody = document.getElementById("results-body")
    tbody.innerHTML = ""

    companies.forEach(company => {
    const row = document.createElement("tr")
    row.className = "clickable"
    row.innerHTML = `
    <td><strong>${company.company}</strong></td>
    <td>${company.reason}</td>
    <td class="score">${company.score}/100</td>  `    
    row.onclick = () => openModal(company)
    tbody.appendChild(row)
    })
}

function openModal(company) {
    document.getElementById("modal-name").textContent = company.company
    document.getElementById("modal-score").textContent = company.score + "/100"
    document.getElementById("modal-what").textContent = company.what_they_do
    document.getElementById("modal-fit").textContent = company.reason
    document.getElementById("modal-culture").textContent = company.culture
    document.getElementById("modal-hiring").textContent = company.hiring_signals
    document.getElementById("modal-overlay").style.display = "block"
}   

function closeModal() {
    document.getElementById("modal-overlay").style.display = "none"
}