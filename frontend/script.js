// Para quando o backend estiver pronto
// const eventsEl = document.getElementById("events");
// async function teste() {
    // const result = await fetch('http://0.0.0.0:8080/events');
    // const events = await result.json()


    const events = [ //Teste
    {
      title: "Teste",
      start_timestamp: new Date(),
      end_timestamp: new Date(),
      all_day: false,
      url: "www.google.com",
      description: "Esse e um evento de teste",
    },
    {
      title: "Teste 2",
      start_timestamp: new Date(),
      end_timestamp: new Date(),
      all_day: true,
      url: "www.event.com",
      description: "2222 Esse e um evento de teste ",
    },
  ];
  
  const listaCards = document.querySelector("#lista-cards");
  
  async function teste() {
    for (const event of events) {
      const section = document.createElement("section");
      // section.classList.add("cg-card-container"); --> Não é necessário por agora
      section.innerHTML = `
          <div class="cg-card-container__card">
          <div class="cg-card-container__card__content">
            <div class="cg-card-container__card__content--left">
              <p class="cg-card-container__card__content--left-day">${event.start_timestamp.getDate()}</p>
              <p class="cg-card-container__card__content--left-month">${event.start_timestamp.getMonth()+1}</p>
              <p class="cg-card-container__card__content--left-year">${event.start_timestamp.getFullYear()}</p>
            </div>
            <div class="cg-card-container__card__content--middle">
              <p class="cg-card-container__card__content--middle-title">${event.title}</p>
              <p class="cg-card-container__card__content--middle-hour">${event.all_day ? "Dia todo": event.start_timestamp.getHours().toString().padStart(2, "0") 
              + ":" + event.start_timestamp.getMinutes().toString().padStart(2, "0") + " - " + event.end_timestamp.getHours().toString().padStart(2, "0") + ":" + event.end_timestamp.getMinutes().toString().padStart(2, "0") }</p>
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