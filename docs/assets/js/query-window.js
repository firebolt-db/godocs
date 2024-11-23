document.addEventListener('DOMContentLoaded', function() {
  if (typeof Prism !== 'undefined') {
    const codeBlocks = document.querySelectorAll('code.firebolt-sql');
    codeBlocks.forEach(block => {
      // Add a non-breaking space if empty
      if (!block.textContent.trim()) {
        block.textContent = ' ';
      }
      
      // Highlight code on load
      Prism.highlightElement(block);
      
      // Re-highlight code on input
      block.addEventListener('input', () => {
        if (!block.textContent.trim()) {
          // We never allow a fully empty code block, this leads to the cursor being in the wrong place
          block.textContent = ' ';
        }
        const pos = saveCaretPosition(block);
        Prism.highlightElement(block);
        restoreCaretPosition(block, pos);
      });
    });
  }
});

// Utility function used by the event listener above to save the caret position
function saveCaretPosition(element) {
  const selection = window.getSelection();
  const range = selection.getRangeAt(0);
  const preSelectionRange = range.cloneRange();
  preSelectionRange.selectNodeContents(element);
  preSelectionRange.setEnd(range.startContainer, range.startOffset);
  return preSelectionRange.toString().length;
}

// Utility function used by the event listener above to restore the caret position
function restoreCaretPosition(element, position) {
  const range = document.createRange();
  const selection = window.getSelection();
  
  let currentPos = 0;
  const walker = document.createTreeWalker(element, NodeFilter.SHOW_TEXT);
  let node;
  
  while ((node = walker.nextNode())) {
    const nodeLength = node.length;
    if (currentPos + nodeLength >= position) {
      range.setStart(node, position - currentPos);
      range.setEnd(node, position - currentPos);
      break;
    }
    currentPos += nodeLength;
  }
  
  selection.removeAllRanges();
  selection.addRange(range);
}

// Function that executes the query on Firebolt whenever the run button is clicked
async function runQuery(button) {
  const queryWindow = button.closest('.query-window');
  const queryInput = queryWindow.querySelector('code.firebolt-sql');
  const resultsDiv = queryWindow.querySelector('.query-results');

  try {
    const queryText = queryInput.textContent || '';
    
    // Send the query to the Firebolt proxy endpoint.
    // TODO(benjamin): Update once we have a real endpoint
    const queryResponse = await fetch('http://localhost:8000/execute-query', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        query: queryText
      })
    });

    // Show the result section
    resultsDiv.classList.remove('hidden');

    const queryResult = await queryResponse.json();
    
    // Check for errors in the response
    if (queryResult.errors && queryResult.errors.length > 0) {
      resultsDiv.innerHTML = `
        <div class="error-message">
          ${queryResult.errors.map(error => 
            `<div class="error-description">${error.description}</div>`
          ).join('')}
        </div>
      `;
      return;
    }

    // Format cell value based on type and value
    const formatCell = (value, type) => {
      if (value === null) return '<span class="null">NULL</span>';
      if (Array.isArray(value)) {
        return `<span class="array">[${value.map(v => 
          v === null ? '<span class="null">NULL</span>' : v
        ).join(', ')}]</span>`;
      }
      if (type.startsWith('double') || type.startsWith('float')) {
        return `<span class="number">${value}</span>`;
      }
      return value;
    };

    // Create result table HTML
    const tableHTML = `
      <div class="table-container">
        ${queryResult.rows === 100 ? 
          '<div class="info-message">For readability, results are limited to 100 rows.</div>' 
          : ''}
        <table class="results-table">
          <thead>
            <tr>
              ${queryResult.meta.map(col => 
                `<th title="Type: ${col.type}">${col.name}</th>`
              ).join('')}
            </tr>
          </thead>
          <tbody>
            ${queryResult.data.map(row => `
              <tr>
                ${row.map((value, index) => 
                  `<td>${formatCell(value, queryResult.meta[index].type)}</td>`
                ).join('')}
              </tr>
            `).join('')}
          </tbody>
        </table>
      </div>
      <div class="query-stats">
        <span>Rows: ${queryResult.rows}</span>
        <span>Time: ${(queryResult.statistics.elapsed * 1000).toFixed(2)}ms</span>
      </div>
    `;
    
    resultsDiv.innerHTML = tableHTML;

  } catch (error) {
    console.error('Error:', error);
    resultsDiv.innerHTML = `<div class="error-message">${error.message}</div>`;
    resultsDiv.classList.remove('hidden');
  }
} 