// Para quando o backend estiver pronto
const eventsEl = document.getElementById("events");
async function teste() {
  const result = await fetch('http://localhost:8000/events');
  const events = await result.json();
  
  const listaCards = document.querySelector("#lista-cards");
  for (const event of events) {
    const section = document.createElement("section");
    // section.classList.add("cg-card-container"); --> Não é necessário por agora
    section.innerHTML = `
        <div class="cg-card-container__card">
        <div class="cg-card-container__card__content">

          <div class="cg-card-container__card__content--middle">
            <p class="cg-card-container__card__content--middle-title">${event.title}</p> 
            <p class="cg-card-container__card__content--middle-adress"> Na terra do nunca </p>
            <p class="cg-card-container__card__content--middle-description">${event.description}</p>
          </div>
          <a href="${event.url}" target="_" title="Veja Mais" class="cg-card-container__card__content--right">Veja mais!</a>
          </div>
        </div>
      </div>

    `;
    // Descobrir por que a URL não está indo corretamente
    // Descobrir como colocar o mês por escrito
    // Falta definir melhor como será puxado a data, mês, ano e horários dos eventos
    // Falta uma variável para puxar o local << 
    listaCards.append(section);
  }
}
teste();