import { MESSAGES } from "./constants";

export default function displayMessages() {
  if (MESSAGES.length === 0) return;
  if (MESSAGES.length > 1) {
    flashTempMessages(MESSAGES);
  }
  MESSAGES[0].classList.add('js-show');
}

function flashTempMessages(messages) {
  messages.forEach((m, i) => {
    const isTempMessage = Boolean(
      m.classList.contains('message--info') || m.classList.contains('message--success')
    );

    m.classList.add('js-show');

    if (isTempMessage) {
      if (i !== messages.length - 1) {
        m.classList.add('js-merge');
      }

      setTimeout(() => {
        m.classList.remove('js-show');
        m.classList.remove('js-merge');
      }, 4000);
    };
  });
}