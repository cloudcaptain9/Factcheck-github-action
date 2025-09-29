document.getElementById("checkBtn").addEventListener("click", async () => {
  const claim = document.getElementById("claim").value.trim();
  const resultDiv = document.getElementById("result");

  if (!claim) {
    resultDiv.innerHTML = "<p style='color:red;'>Please enter a claim.</p>";
    return;
  }

  resultDiv.innerHTML = "<p>Checking claim...</p>";

  try {
    const response = await fetch("/factcheck", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ claim })
    });

    const data = await response.json();

    if (data.error) {
      resultDiv.innerHTML = `<p style="color:red;">Error: ${data.error}</p>`;
    } else {
      // Backend returns {"result": "...JSON string..."}
      let parsed;
      try {
        parsed = JSON.parse(data.result);
      } catch (e) {
        parsed = { verdict: "Unclear", reason: data.result };
      }

      resultDiv.innerHTML = `
        <h3>Verdict: ${parsed.verdict}</h3>
        <p><strong>Reason:</strong> ${parsed.reason}</p>
      `;
    }
  } catch (err) {
    resultDiv.innerHTML = `<p style="color:red;">Error: ${err.message}</p>`;
  }
});
