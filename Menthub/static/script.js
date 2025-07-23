document.addEventListener("DOMContentLoaded", function () {
    const container = document.querySelector(".container");
    const signupBtn = document.querySelector(".green-bg button");
    const loginBtn = document.querySelector(".orange-bg button");

    signupBtn.addEventListener("click", () => {
        container.classList.add("change");
    });

    loginBtn.addEventListener("click", () => {
        container.classList.remove("change");
    });

    // ✅ Match button logic
    const matchBtn = document.getElementById("matchBtn");
    const resultDiv = document.getElementById("result");

    if (matchBtn && resultDiv) {
        matchBtn.addEventListener("click", function () {
            fetch("http://localhost:5000/match")
                .then(response => response.json())
                .then(data => {
                    resultDiv.innerHTML = "";

                    if (data.length === 0) {
                        resultDiv.innerHTML = "<p>No matches found.</p>";
                        return;
                    }

                    data.forEach(pair => {
                        const pairDiv = document.createElement("div");
                        pairDiv.classList.add("match-result");

                        pairDiv.innerHTML = `
                            <h3>Mentor:</h3>
                            <p>Name: ${pair.mentor.name}</p>
                            <p>Email: ${pair.mentor.email}</p>

                            <h3>Mentee:</h3>
                            <p>Name: ${pair.mentee.name}</p>
                            <p>Email: ${pair.mentee.email}</p>
                            <hr />
                        `;

                        resultDiv.appendChild(pairDiv);
                    });
                })
                .catch(error => {
                    console.error("Error fetching matches:", error);
                    resultDiv.innerHTML = "<p>Error fetching matches. Try again later.</p>";
                });
        });
    }
});
