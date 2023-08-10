import { COVER_AMOUNT_INPUT, COVER_AMOUNT_LABEL, COVER_CHARGE_INPUTS } from "./constants";

export default function displayCoverAmountInput(checkedValue) {
  const isOnChange = Boolean(checkedValue);
  
  if (!isOnChange) {
    COVER_CHARGE_INPUTS.forEach(input => {
      if (input.hasAttribute('checked') && input.value === 'Yes') {
        COVER_AMOUNT_INPUT.classList.add('show');
        COVER_AMOUNT_LABEL[0].classList.add('show');
        COVER_AMOUNT_INPUT.setAttribute('required', '');
      };
    });
  }
  
  if (checkedValue == 'Yes') {
    COVER_AMOUNT_INPUT.classList.add('show');
    COVER_AMOUNT_LABEL[0].classList.add('show');
    COVER_AMOUNT_INPUT.setAttribute('required', '');
    COVER_AMOUNT_INPUT.required = true;
    COVER_AMOUNT_INPUT.insertAdjacentHTML(
      'beforebegin', "<span style='color:red;'>*</span>"); 
  }
  if (checkedValue == 'No' && COVER_AMOUNT_INPUT.classList.contains('show')) {
    COVER_AMOUNT_INPUT.classList.remove('show');
    COVER_AMOUNT_LABEL[0].classList.remove('show');
    COVER_AMOUNT_INPUT.required = false;
    COVER_AMOUNT_INPUT.value = null;
    COVER_AMOUNT_INPUT.previousElementSibling.remove();
  }
};