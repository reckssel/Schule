// Menü auf dem Handy öffnen/schließen
const menuBtn = document.getElementById("menuBtn");
const navLinks = document.getElementById("navLinks");

menuBtn.addEventListener("click", () => {
  navLinks.classList.toggle("offen");
});

// Menü schließen, wenn ein Link angeklickt wird
navLinks.querySelectorAll("a").forEach((link) => {
  link.addEventListener("click", () => navLinks.classList.remove("offen"));
});

// Kontaktformular (Beispiel – es wird nichts wirklich verschickt)
const form = document.getElementById("kontaktForm");
const meldung = document.getElementById("meldung");

form.addEventListener("submit", (e) => {
  e.preventDefault();
  const name = form.name.value.trim();
  meldung.textContent = `Danke, ${name}! Ihre Nachricht ist angekommen – Status 200 OK statt 404 😉`;
  form.reset();
});
