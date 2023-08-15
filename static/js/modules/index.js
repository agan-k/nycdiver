import { 
  DESCRIPTION_PARAGRAPH_SELECTOR,
  FIELD_CONTENT_PHONE } from "./constants";
import { 
  onChange, 
  getCopyrightYear,
} from "./utils";
import denoteRequiredFormFields from "./denoteRequiredFormFields";
import displayCoverAmountInput from "./displayCoverAmountInput";
import toggleExpandListings from "./toggleExpandListings";
import setForScreenWidth from "./setForScreenWidth";
import toggleOpenNavigation from "./toggleOpenNavigation";
import setBgImagePosition from "./setBgImagePosition";
import formatText from "./formatText";
import displayMessages from "./displayMessages";
import disableExternalLinks from "./disableExternalLinks";

setForScreenWidth();
setBgImagePosition();
getCopyrightYear();
onChange(displayCoverAmountInput);
displayCoverAmountInput();
displayMessages();
disableExternalLinks();
toggleOpenNavigation();
toggleExpandListings();
denoteRequiredFormFields();
formatText([
  DESCRIPTION_PARAGRAPH_SELECTOR, 
  FIELD_CONTENT_PHONE]);

