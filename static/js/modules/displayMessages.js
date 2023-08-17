import { MESSAGES } from "./constants";

export default function displayMessages() {
  if (MESSAGES.length === 0) return;

  MESSAGES.forEach((m, index) => {
    const isTempMessage = Boolean(
      m.classList.contains('message--info') || 
      m.classList.contains('message--success'));
    const hasMultipleMessages = Boolean(MESSAGES.length > 1);
    setTimeout(() => {
      m.classList.add('js-show');
    }, 100)

    if (isTempMessage && hasMultipleMessages) {
      if (index !== MESSAGES.length - 1) {
        m.classList.add('js-merge');
      }
      setTimeout(() => {
        m.classList.remove('js-show');
        m.classList.remove('js-merge');
      }, 4500);
    };
    if (isTempMessage) {
      setTimeout(() => {
        m.classList.remove('js-show');
      }, 3000);
    }
  });
}
