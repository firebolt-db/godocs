var codeBlocks = document.querySelectorAll('pre.highlight');

codeBlocks.forEach(function (codeBlock) {
  var copyButton = document.createElement('button');
  copyButton.className = 'copy';
  copyButton.type = 'button';
  copyButton.ariaLabel = 'Copy code to clipboard';
  copyButton.innerHTML = '<img src="../../assets/images/copy_icon.svg" />';

  codeBlock.append(copyButton);

  copyButton.addEventListener('click', function () {
    var code = codeBlock.querySelector('code').innerText.trim();
    window.navigator.clipboard.writeText(code);

    copyButton.innerHTML = '<img src="../docs/assets/images/success.svg" />';
    var twoSeconds = 2000;

    setTimeout(function () {
      copyButton.innerHTML = '<img src="../docs/assets/images/copy_icon.svg" />';
    }, twoSeconds);
  });
});