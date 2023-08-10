import { MESSAGES_INFO } from "./constants";

export default function hideInfoMessages() {
  MESSAGES_INFO.forEach(message => {
    setTimeout(() => {
      message.classList.add('js-hide')
    }, 2500)
  })
}