import { RESPONSIVE_ELEMENTS } from "./constants";

export default function setForScreenWidth() {
  const isMobile = Boolean(window.screen.width < 400);
  RESPONSIVE_ELEMENTS.forEach(element => {
    if (isMobile) element.classList.add('js-mobile');
    if (!isMobile &&  element.classList.contains('js-mobile')) {
        element.classList.remove('js-mobile');
      }
  })
  return isMobile;
};