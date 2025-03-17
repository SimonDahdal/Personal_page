document.addEventListener("DOMContentLoaded", () => {
  const keywords = ["Simon", "Dahdal"]; 
  const liElements = document.querySelectorAll("li");
  liElements.forEach(li => {
    keywords.forEach(word => {
      const regex = new RegExp(word, "gi");
      li.innerHTML = li.innerHTML.replace(regex, match => `<strong>${match}</strong>`);
    });
  });
});
