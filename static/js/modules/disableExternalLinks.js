import { EXTERNAL_LINKS } from "./constants";

export default function disableExternalLinks() {
  EXTERNAL_LINKS.forEach(l => {
    if (l.classList.contains('disabled')) l.href = '';
  })
}