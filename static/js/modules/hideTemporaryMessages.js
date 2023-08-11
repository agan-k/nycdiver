import { MESSAGES_TEMPORARY } from "./constants";

export default function hideTemporaryMessages() {
  MESSAGES_TEMPORARY.forEach(message => {
    setTimeout(() => {
      message.classList.add('js-hide')
    }, 2500)
  })
}