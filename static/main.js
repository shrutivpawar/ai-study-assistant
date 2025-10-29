async function postJSON(url, payload) {
  const res = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  });
  return res.json();
}

function show(text) {
  const out = document.getElementById("output");
  out.innerHTML = `<pre>${text}</pre>`;
}

document.getElementById("btnSumm").addEventListener("click", async () => {
  const text = document.getElementById("inputText").value.trim();
  if (!text) return alert("Paste some notes first.");
  show("Working...");
  const resp = await postJSON("/api/summarize", { text });
  if (resp.error) show("Error: " + resp.error);
  else show(resp.result);
});

document.getElementById("btnExplain").addEventListener("click", async () => {
  const text = document.getElementById("inputText").value.trim();
  if (!text) return alert("Paste some notes first.");
  show("Working...");
  const resp = await postJSON("/api/explain", { text, level: "college" });
  if (resp.error) show("Error: " + resp.error);
  else show(resp.result);
});

document.getElementById("btnQuiz").addEventListener("click", async () => {
  const text = document.getElementById("inputText").value.trim();
  if (!text) return alert("Paste some notes first.");
  show("Working...");
  const resp = await postJSON("/api/quiz", { text, count: 3 });
  if (resp.error) show("Error: " + resp.error);
  else show(resp.result);
});