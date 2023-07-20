// 支援物資データ
var supportItems = {
    'medical-items': ['松葉杖', '車椅子', '歩行器'],
    'dietary-items': ['アレルギー食品', '低塩分食品', '糖尿病管理のための特別な食品'],
    'baby-items': ['ベビーベッド', 'ベビーフード', '紙おむつ', 'ミルク'],
    'feminine-items': ['生理用ナプキン', 'タンポン', 'パッド'],
    'psychological-items': ['心理カウンセリング', '心理的な安心感を与えるアイテム'],
    'learning-items': ['学校教材', '学習ツール'],
    'clothing-items': ['季節に応じた衣類']
  };
  
  // 支援物資要望フォームの生成
  function generateSupportForm() {
    for (var key in supportItems) {
      var itemList = supportItems[key];
      var ulElement = document.getElementById(key);
      
      for (var i = 0; i < itemList.length; i++) {
        var liElement = document.createElement('li');
        var checkboxElement = document.createElement('input');
        checkboxElement.type = 'checkbox';
        checkboxElement.name = key;
        checkboxElement.value = itemList[i];
        
        var labelElement = document.createElement('label');
        labelElement.appendChild(checkboxElement);
        labelElement.appendChild(document.createTextNode(itemList[i]));
        
        liElement.appendChild(labelElement);
        ulElement.appendChild(liElement);
      }
    }
  }
  
  // フォームの送信処理
  function submitForm() {
    var formElements = document.querySelectorAll('#support-items input[type="checkbox"]');
    var selectedItems = [];
    
    for (var i = 0; i < formElements.length; i++) {
      if (formElements[i].checked) {
        selectedItems.push(formElements[i].value);
      }
    }
    
    // 選択された支援物資の処理を行う（例えばサーバーに送信するなど）
    console.log('選択された支援物資:', selectedItems);
  }
  
  // フォームの生成を実行
  generateSupportForm();
  