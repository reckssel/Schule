// ===== Menü auf dem Handy =====
const menuBtn = document.getElementById("menuBtn");
const navLinks = document.getElementById("navLinks");

menuBtn.addEventListener("click", () => navLinks.classList.toggle("offen"));
navLinks.querySelectorAll("a").forEach((link) => {
  link.addEventListener("click", () => navLinks.classList.remove("offen"));
});

// ===== Elemente beim Scrollen einblenden =====
const beobachter = new IntersectionObserver((eintraege) => {
  eintraege.forEach((e) => {
    if (e.isIntersecting) {
      e.target.classList.add("sichtbar");
      beobachter.unobserve(e.target);
    }
  });
}, { threshold: 0.15 });
document.querySelectorAll(".einblenden").forEach((el) => beobachter.observe(el));

// ===== Zahlen hochzählen =====
function hochzaehlen(el) {
  const ziel = parseFloat(el.dataset.ziel);
  const komma = parseInt(el.dataset.komma || "0");
  const dauer = 1500;
  const start = performance.now();
  function schritt(jetzt) {
    const anteil = Math.min((jetzt - start) / dauer, 1);
    el.textContent = (ziel * anteil).toFixed(komma).replace(".", ",");
    if (anteil < 1) requestAnimationFrame(schritt);
  }
  requestAnimationFrame(schritt);
}
const zahlenBeobachter = new IntersectionObserver((eintraege) => {
  eintraege.forEach((e) => {
    if (e.isIntersecting) {
      e.target.querySelectorAll(".zaehler").forEach(hochzaehlen);
      zahlenBeobachter.unobserve(e.target);
    }
  });
});
zahlenBeobachter.observe(document.querySelector(".zahlen"));

// ===== Live-Status (Beispiel mit Zufallswerten) =====
const statusBtn = document.getElementById("statusBtn");
const statusZeit = document.getElementById("statusZeit");
const statusElemente = document.querySelectorAll("#statusListe .status");

function statusPruefen() {
  statusElemente.forEach((el) => {
    el.className = "status pruefe";
    el.textContent = "Prüfe…";
  });
  setTimeout(() => {
    statusElemente.forEach((el) => {
      // 90 % Chance auf "Online", sonst "Wartung"
      if (Math.random() < 0.9) {
        el.className = "status ok";
        el.textContent = "Online";
      } else {
        el.className = "status warn";
        el.textContent = "Wartung";
      }
    });
    statusZeit.textContent = new Date().toLocaleTimeString("de-DE");
  }, 1000);
}
statusBtn.addEventListener("click", statusPruefen);
statusZeit.textContent = new Date().toLocaleTimeString("de-DE");

// ===== Preise: monatlich / jährlich =====
const preisToggle = document.getElementById("preisToggle");
preisToggle.addEventListener("change", () => {
  document.querySelectorAll(".betrag").forEach((el) => {
    const preis = parseFloat(el.dataset.preis);
    el.textContent = preisToggle.checked ? Math.round(preis * 0.85) : preis;
  });
});

// ===== Kostenrechner =====
const plaetze = document.getElementById("plaetze");
const plaetzeWert = document.getElementById("plaetzeWert");
const paketWahl = document.getElementById("paketWahl");
const ergebnis = document.getElementById("ergebnis");

function rechnen() {
  const anzahl = parseInt(plaetze.value);
  const preis = parseInt(paketWahl.value);
  plaetzeWert.textContent = anzahl;
  ergebnis.textContent = (anzahl * preis).toLocaleString("de-DE") + " €";
}
plaetze.addEventListener("input", rechnen);
paketWahl.addEventListener("change", rechnen);
rechnen();

// ===== Kundenstimmen-Slider =====
const bewertungen = document.querySelectorAll(".bewertung");
const punkteBox = document.getElementById("punkte");
let aktuell = 0;

bewertungen.forEach((_, i) => {
  const punkt = document.createElement("button");
  punkt.setAttribute("aria-label", "Bewertung " + (i + 1));
  punkt.addEventListener("click", () => zeige(i));
  punkteBox.appendChild(punkt);
});

function zeige(index) {
  aktuell = (index + bewertungen.length) % bewertungen.length;
  bewertungen.forEach((b, i) => b.classList.toggle("aktiv", i === aktuell));
  punkteBox.querySelectorAll("button").forEach((p, i) => p.classList.toggle("aktiv", i === aktuell));
}
document.getElementById("weiter").addEventListener("click", () => zeige(aktuell + 1));
document.getElementById("zurueck").addEventListener("click", () => zeige(aktuell - 1));
setInterval(() => zeige(aktuell + 1), 6000);
zeige(0);

// ===== Kontaktformular (Beispiel – es wird nichts verschickt) =====
const form = document.getElementById("kontaktForm");
const meldung = document.getElementById("meldung");
form.addEventListener("submit", (e) => {
  e.preventDefault();
  const name = form.name.value.trim();
  meldung.textContent = `Danke, ${name}! Ihre Nachricht ist angekommen – Status 200 OK statt 404 😉`;
  form.reset();
});

// ===== Newsletter =====
document.getElementById("newsletterForm").addEventListener("submit", (e) => {
  e.preventDefault();
  document.getElementById("newsletterMeldung").textContent = "Danke fürs Anmelden!";
  e.target.reset();
});

// ===== Nach-oben-Button =====
const nachOben = document.getElementById("nachOben");
window.addEventListener("scroll", () => {
  nachOben.classList.toggle("sichtbar", window.scrollY > 600);
});
nachOben.addEventListener("click", () => window.scrollTo({ top: 0, behavior: "smooth" }));
