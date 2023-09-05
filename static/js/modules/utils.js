export const onChange = (f) => {
  const fName = f.name
  window[fName] = f;
};

export const styleElement = (element, style) => {
  for (const property in style)
      element.style[property] = style[property];
}


export const getCopyrightYear = () => {
  document.getElementById('copyright').innerHTML = `&copy;${new Date().getFullYear()}`;
}

export function formatFieldContent(field) {
  field.forEach(field => {
    let content = field.textContent;
    const formattedField = 
    '(' + content.slice(0, 3) + ')' + ' ' + content.slice(3, 6) + ' ' + content.slice(6);
    field.textContent = formattedField;
  });
}

export const splitDescriptionParagraphs = (selector) => {
  const nodes = document.querySelectorAll(selector);
  nodes.forEach(node => {
    const text = node.textContent;
    const paragraphs = text.split('\n\n');
    
    const formattedSummary = paragraphs.map(p => {
      const para = document.createElement('p');
      para.textContent = p;
      return para;
    });
    
    node.replaceChildren(...formattedSummary);
  })
};
