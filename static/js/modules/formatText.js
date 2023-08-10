import { DESCRIPTION_PARAGRAPH_SELECTOR, FIELD_CONTENT_HEADLINER_AND_VENUE, FIELD_CONTENT_PHONE } from "./constants";
import { splitDescriptionParagraphs, formatFieldContent } from "./utils";

export default function formatText([...selector]) {
  selector.forEach(item => {
    if (item === DESCRIPTION_PARAGRAPH_SELECTOR) {
      splitDescriptionParagraphs(item)
    }
    if (item === FIELD_CONTENT_PHONE) {
      formatFieldContent(item)
    }
  })
}