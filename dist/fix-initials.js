// Fix client initial areas for better printing
document.addEventListener('DOMContentLoaded', function() {
  // Find all paragraphs with "Client acknowledgment" text
  const clientInitialParagraphs = Array.from(document.querySelectorAll('p'))
    .filter(p => p.textContent.includes('Client acknowledgment') || 
                 p.textContent.includes('Client initials'));
  
  // Apply special styling to these paragraphs
  clientInitialParagraphs.forEach(p => {
    p.classList.add('client-initials');
    
    // Add padding and consistent line for signatures
    const text = p.innerHTML;
    p.innerHTML = text.replace(
      /(Client.*): \_\_\_\_\_\_\_\_/g, 
      '$1: <span style="display:inline-block; min-width: 200px; border-bottom: 1px solid #000;">&nbsp;</span>'
    );
  });
  
  // Fix checkboxes
  const checkboxTexts = Array.from(document.querySelectorAll('p'))
    .filter(p => p.textContent.includes('□'));
    
  checkboxTexts.forEach(p => {
    p.innerHTML = p.innerHTML.replace(/□/g, '<span class="checkbox">☐</span>');
  });
  
  // Add page breaks before major sections
  const majorSections = Array.from(document.querySelectorAll('p strong'))
    .filter(s => s.textContent.match(/^\d{1,2}\./))
    .map(s => s.parentElement);
  
  // Add page break before sections 7, 13, 18
  const breakSections = [7, 13, 18];
  majorSections.forEach(section => {
    const sectionText = section.textContent;
    const sectionMatch = sectionText.match(/^(\d{1,2})\./);
    
    if (sectionMatch && breakSections.includes(parseInt(sectionMatch[1]))) {
      section.classList.add('page-break-before');
    }
  });
}); 