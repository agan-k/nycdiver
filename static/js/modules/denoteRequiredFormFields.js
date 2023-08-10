export default function denoteRequiredFormFields() {
  const form = document.querySelector('.form-event-add-or-update');
  if (!form) return;
  const requiredFields = form.querySelectorAll("[required]");
    requiredFields.forEach(field => {
      if (field.id === 'id_cover_charge_0') {
        field.parentNode.parentNode.parentNode.insertAdjacentHTML('beforebegin', "<span style='color:red;'>*</span>"); 
      } 
      if (field.id === 'id_cover_charge_0' || field.id === 'id_cover_charge_1') {
        field.insertAdjacentHTML('beforebegin', "<span style='visibility:hidden;'>*</span>");
      } else if (field.previousElementSibling.tagName === 'UL') {
        field.previousElementSibling.insertAdjacentHTML('beforebegin', "<span style='color:red;'>*</span>"); 
      } else {
        field.insertAdjacentHTML('beforebegin', "<span style='color:red;'>*</span>"); 
      }
  });
};