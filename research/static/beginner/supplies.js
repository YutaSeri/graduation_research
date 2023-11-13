const form = document.getElementById('categoryForm');

form.addEventListener('submit', e => {

  e.preventDefault();

  // カテゴリを取得
  const categories = JSON.parse(sessionStorage.getItem('categories'));
  
  // 個数を取得
  const quantity = document.getElementById('quantity').value;

  alert(`カテゴリ: ${categories} 
  個数: ${quantity}`);

});