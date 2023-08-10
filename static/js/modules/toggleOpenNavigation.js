import { NAV_ROW_ELEMENTS } from "./constants"

export default function toggleOpenNavigation() {
  NAV_ROW_ELEMENTS.forEach(element => {
      element.addEventListener('click', e => {
        e.stopPropagation();
        e.currentTarget.classList.toggle('js-open')
        NAV_ROW_ELEMENTS.forEach(item => {
          if (item !== e.currentTarget) item.classList.remove('js-open');
        })
      })
    })
    handleOuterClicks();
};

function handleOuterClicks() {
  const outerElements = document.querySelectorAll('.page-wrapper, body');
  outerElements.forEach(element => {
    element.addEventListener('click', e => {
      NAV_ROW_ELEMENTS.forEach(item => {
        if (item !== e.currentTarget && item.classList.contains('js-open')) item.classList.remove('js-open');
      })
    })
  })
}