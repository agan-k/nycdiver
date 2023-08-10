import { EVENT_LISTINGS } from "./constants";

export default function toggleExpandListings() {
  EVENT_LISTINGS.forEach(listing => {
    const eventCardHeadings = listing.querySelectorAll('.event-card__heading, .event-card__heading--small');
    toggleTruncateHeading(eventCardHeadings);
    listing.addEventListener('click', e => {
      const activeListing = e.currentTarget;
      const activeHeadings = activeListing.querySelectorAll('.event-card__heading, .event-card__heading--small');
      activeListing.classList.toggle('js-expand');
      toggleTruncateHeading(activeHeadings);
      closeOtherListings(e);

    })
  });
};

function toggleTruncateHeading(headings) {
  headings.forEach(heading => {
    if (heading.textContent.length > 17) {
      heading.classList.toggle('js-truncate')
      //TODO: figure out how to truncate with trailing dots:
      // heading.textContent = heading.textContent.slice(0, 17) + ' ...'
    }
  });
}

function closeOtherListings(event) {
  EVENT_LISTINGS.forEach(listing => {
    if(listing.id !== event.currentTarget.id && listing.classList.contains('js-expand')) {
      const activeHeadings = listing.querySelectorAll('.event-card__heading, .event-card__heading--small');
      listing.classList.remove('js-expand');
      toggleTruncateHeading(activeHeadings);
    };
  });
}