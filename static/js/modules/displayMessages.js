import { MESSAGES } from "./constants";

export default function displayMessages() {
  if (MESSAGES.length === 0) return;

  MESSAGES.forEach((m, index) => {
    const isTempMessage = Boolean(
    m.classList.contains('message--info') || 
    m.classList.contains('message--success'));
    const hasMultipleMessages = Boolean(MESSAGES.length > 1);

    m.classList.add('js-show');

    if (isTempMessage && hasMultipleMessages) {
      if (index !== MESSAGES.length - 1) {
        m.classList.add('js-merge');
      }
      setTimeout(() => {
        m.classList.remove('js-show');
        m.classList.remove('js-merge');
      }, 4000);
    };
    if (isTempMessage) {
      setTimeout(() => {
        m.classList.remove('js-show');
      }, 4000);
    }
  });
}
