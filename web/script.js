document.addEventListener("DOMContentLoaded", function () {
  const slider = document.querySelector('.slider'); 
  const sliderContainer = slider.querySelector('.slider-container');
  const slides = sliderContainer.querySelectorAll('.slide');
  const prevBtn = slider.querySelector('.arrow.prev');
  const nextBtn = slider.querySelector('.arrow.next');

  let currentIndex = 0;

  function showSlide(index) {
      slides.forEach((slide, i) => {
          if (i === index) {
              slide.style.display = 'block';
          } else {
              slide.style.display = 'none';
          }
      });
  }

  function nextSlide() {
      currentIndex = (currentIndex === slides.length - 1) ? 0 : currentIndex + 1;
      showSlide(currentIndex);
  }

  function prevSlide() {
      currentIndex = (currentIndex === 0) ? slides.length - 1 : currentIndex - 1;
      showSlide(currentIndex);
  }

  nextBtn.addEventListener('click', nextSlide);
  prevBtn.addEventListener('click', prevSlide);


  setInterval(nextSlide, 2000);
  const eventsEl = document.getElementById("lista-cards");
  let eventCards = [];

  async function fetchEvents() {
    const response = await fetch("http://localhost:8000/events");
    const eventsData = await response.json();

    if (response.ok) {
      eventCards = eventsData.map(createEventCard);
      displayEvents(eventCards);
    } else {
      console.error("Error fetching events:", response.statusText);
    }
  }

  function createEventCard(event) {
    const section = document.createElement("section");
    section.classList.add("cg-card-section");

    const startDate = new Date(event.start_timestamp);
    const day = startDate.getDate();
    const month = startDate.getMonth();
    const year = startDate.getFullYear();
    const startHour = startDate.getHours();
    const startMinutes = startDate.getMinutes();

    const endDate = new Date(event.end_timestamp);
    const endHour = endDate.getHours();
    const endMinutes = endDate.getMinutes();
    const all_day = event.all_day;
    const title = event.title;
    const city = event.city;
    const linkEvent = event.url;

    const monthNames = [
      "janeiro",
      "fevereiro",
      "março",
      "abril",
      "maio",
      "junho",
      "julho",
      "agosto",
      "setembro",
      "outubro",
      "novembro",
      "dezembro",
    ];

    section.innerHTML = `
    <div class="cg-card-container__card">
      <div class="cg-card-container__card__content--date">
        <p class="cg-card-container__card__content--date-day">${day}</p>
        <p class="cg-card-container__card__content--date-month">
          ${monthNames[month]}
        </p>
        <p class="cg-card-container__card__content--date-year">${year}</p>
      </div>
      <div class="cg-card-container__card__description--top">
        <p class="cg-card-container__card__description--title">${title}</p>
      </div>
      <div class="cg-card-container__card__description--address">
        <p class="cg-card-container__card__description--description">
          ${event.description}
        </p>
        <p class="cg-card-container__card__description--address-line">
          <span class="bold-text"> Endereço: </span> ${event.address}
        </p>
        <div class="cg-card-container__card__description--container">
          <div class="cg-card-container__card__description--time">
            <p  class="cg-card-container__card__description--time">
              ${startHour + startMinutes} h
            </p>
            <p class="cg-card-container__card__description--time"> - </p>
            <p class="cg-card-container__card__description--time">
              ${endHour + endMinutes} h
            </p>
          </div>
          ${
            all_day
              ? `<p class="cg-card-container__card__description--period">O dia todo</p>`
              : `<p class="cg-card-container__card__description--period">Meio período</p>`
          }
          <p class="cg-card-container__card__description--city">${city}</p>
        </div>
      </div>
      <div class="cg-card-container__card__description--link-container">
        <a class="cg-card-container__card__description--link" href=${linkEvent}>Veja mais!</a>
      </div>
    </div>
    `;
    return section;
  }

  function displayEvents(events) {
    eventsEl.innerHTML = "";
    eventsEl.append(...events);
  }

  function filterEvents(cityFilter) {
    const filteredEvents = eventCards.filter((card) => {
      const eventData = getEventDataFromCard(card);
      const isCityMatch = cityFilter === "" || eventData.city === cityFilter;
      return isCityMatch;
    });
    displayEvents(filteredEvents);
  }

  function getEventDataFromCard(card) {
    const cityElement = card.querySelector(".cg-card-container__card__description--city");
    const city = cityElement.textContent.trim();
    return { city };
  }

  const cityFilter = document.getElementById("city-filter");
  cityFilter.addEventListener("change", function () {
    filterEvents(this.value);
  });

  fetchEvents();
});
