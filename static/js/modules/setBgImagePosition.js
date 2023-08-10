import setForScreenWidth from "./setForScreenWidth";
import { BODY } from "./constants";

export default function setBgImagePosition() {
  const isMobile = setForScreenWidth();
  if (isMobile) {
    BODY.style.backgroundPosition = 'top 100px center';
    BODY.style.backgroundSize = '115%';
  }
}