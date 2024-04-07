const events = [
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
      // section.classList.add("cg-card-container");
      section.innerHTML = `
          <div class="cg-card-container__card">
          <div class="cg-card-container__card__content">
            <div class="cg-card-container__card__content--left">
              <p class="cg-card-container__card__content--left-day">${event.start_timestamp.getDay()}</p>
              <p class="cg-card-container__card__content--left-month">${event.start_timestamp.getMonth()}</p>
              <p class="cg-card-container__card__content--left-year">${event.start_timestamp.getFullYear()}</p>
            </div>
            <div class="cg-card-container__card__content--middle">
              <p class="cg-card-container__card__content--middle-title">${event.title}</p>
              <p class="cg-card-container__card__content--middle-hour">${event.all_day ? "Dia todo": event.start_timestamp.getHours().toString().padStart(2, "0") 
              + ":" + event.start_timestamp.getMinutes().toString().padStart(2, "0")}</p>
              <p class="cg-card-container__card__content--middle-adress"> Na casa do caralho </p>
              <p class="cg-card-container__card__content--middle-description">${event.description}</p>
            </div>
            <a href="${event.url}" target="_" title="Veja Mais" class="cg-card-container__card__content--right">Veja mais!</a>
            </div>
          </div>
        </div>
  
      `;
      listaCards.append(section);
    }
  }
  
  teste();