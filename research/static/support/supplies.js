$(document).ready(function () {
  var selectedCategory = null;
  var selectedSubCategory1 = null;
  var selectedSubCategory2 = null;

  function rememberSecondSubCategory() {
    // 選択したサブカテゴリを対応する変数に記憶する
    var subCategoryInput = $('input[name=subCategory]:checked');
    var subSubCategoryInput = $('input[name=subSubCategory]:checked');
    var sub3CategoryInput = $('input[name=sub3Category]:checked');

    selectedSubCategory1 = subCategoryInput.length ? subCategoryInput.val() : null;
    selectedSubCategory2 = subSubCategoryInput.length ? subSubCategoryInput.val() : null;
  }

  $('input[type=radio][name=category]').change(function () {
    selectedCategory = this.value;
    switch (selectedCategory) {
      case '医療・介護用品':
        showSubCategory(['松葉杖', '車椅子', '歩行器', '大人用おむつ', 'テキスト入力']);
        break;
      case '食料品':
        showSubCategory(['パン', 'カップめん', '水', 'アレルギー食品', 'テキスト入力']);
        break;
      case '幼児用品':
        showSubCategory(['ベビーフード', '紙おむつ', 'ミルク', 'ベビーベッド', 'テキスト入力']);
        break;
      case 'その他':
        showSubCategory(['衣服品', '靴', 'トイレットペーパー', '毛布', '携帯トイレ', 'テキスト入力']);
        break;
      default:
        selectedCategory = null; // カテゴリをリセット
        selectedSubCategory1 = null; // サブカテゴリをリセット
        selectedSubCategory2 = null;
        $('#subCategory').html('');
        $('#subSubCategory').html('');
        $('#itemDetails').html('');
    }
  });

  $(document).on('change', 'input[name=subCategory]', function () {
    selectedSubCategory1 = this.value;
    switch (selectedSubCategory1) {
      case '松葉杖':
        $('#itemDetails').html('身長：<input type="text" name="height">cm');
        break;
      case '車椅子':
        showSubSubCategory(['大型', '中型', '小型']);
        break;
      case '歩行器':
        showSubSubCategory(['サークル型', '四輪歩行者']);
        break;
      case '大人用おむつ':
        showSubSubCategory(['S','M','L']);
        break;
      case 'アレルギー食品':
        $('#itemDetails').html('<input type="checkbox" name="allergen" value="えび">えび' +
          '<input type="checkbox" name="allergen" value="かに">かに' +
          '<input type="checkbox" name="allergen" value="くるみ">くるみ' +
          '<input type="checkbox" name="allergen" value="小麦">小麦' +
          '<input type="checkbox" name="allergen" value="そば">そば' +
          '<input type="checkbox" name="allergen" value="卵">卵' +
          '<input type="checkbox" name="allergen" value="牛乳">牛乳' +
          '<input type="checkbox" name="allergen" value="落花生">落花生' +
          'その他：<input type="text" name="others">');
        break;
      case '衣服品':
        showSubSubCategory(['上着', 'ズボン']);
        break;
      case '靴':
        showSubSubCategory(['運動靴', '長靴']);
        break;
      case 'テキスト入力':
        $('#itemDetails').html('テキスト入力：<input type="text" name="others">');
        break;
      default:
        $('#itemDetails').html('');
        $('#subSubCategory').html('');
    }

    rememberSecondSubCategory();
  });

  $(document).on('change', 'input[name=subSubCategory]', function () {
    selectedSubCategory2 = this.value;
    switch (selectedSubCategory2) {
      case '上着':
        showSub3Category(['半袖', '長袖']);
        break;
      case 'ズボン':
        showSub3Category(['半ズボン', '長ズボン']);
        break;
      case '運動靴':
      case '長靴':
        showSizeOptions(['15cm','16cm','17cm','18cm','19cm','20cm','21cm','22cm','23cm','23.5cm','24cm','24.5cm','25cm','25.5cm','26cm','26.5cm','27cm','27.5cm','28cm','28.5cm','29cm','29.5cm','30cm']);
        break;
    }
 
    rememberSecondSubCategory();
  });

  $(document).on('change', 'input[name=sub3Category]', function () {
    var clothingCategory = this.value;
    switch (clothingCategory) {
      case '半袖':
      case '長袖':
      case '半ズボン':
      case '長ズボン':
        showSizeOptions(['120cm', '130cm', '140cm', '150cm', '160cm', 'XS', 'S', 'M', 'L', 'XL', '2XL', '3XL', '4XL']);
        break;
      default:
        $('#subSubCategory').html('');
        $('#itemDetails-2').html('');
    }

    rememberSecondSubCategory();
  });

  function showSubCategory(subCategories) {
    var subCategoryHTML = '';
    for (var i = 0; i < subCategories.length; i++) {
      subCategoryHTML += '<input type="radio" name="subCategory" value="' + subCategories[i] + '">' + subCategories[i] + '';
    }

    $('#subCategory').html(subCategoryHTML);

    if (selectedSubCategory1) {
      $('input[name=subCategory][value="' + selectedSubCategory1 + '"]').prop('checked', true);
    }

    $('#subSubCategory').html(''); // サブサブカテゴリをリセット
    $('#itemDetails').html(''); // アイテム詳細をリセット
  }

  function showSubSubCategory(subSubCategories) {
    var subSubCategoryHTML = '';
    for (var i = 0; i < subSubCategories.length; i++) {
      subSubCategoryHTML += '<input type="radio" name="subSubCategory" value="' + subSubCategories[i] + '">' + subSubCategories[i] + '';
    }
    // サブサブカテゴリを表示する前に選択した値を記憶
    var rememberedValue = $('input[name=subSubCategory]:checked').val();
    $('#subSubCategory').html(subSubCategoryHTML); // サブサブカテゴリを表示
    // 選択されていれば選択状態を保持
    if (rememberedValue) {
      $('input[name=subSubCategory][value="' + rememberedValue + '"]').prop('checked', true);
      selectedSubCategory2 = rememberedValue; // 選択したサブサブカテゴリを記憶
    } else {
      selectedSubCategory2 = null; // 選択されているサブサブカテゴリがない場合はリセット
    } 
    $('#itemDetails').html(''); // アイテム詳細をリセット
  }
  function showSub3Category(sub3Categories) {
    var sub3CategoryHTML = '';
    for (var i = 0; i < sub3Categories.length; i++) {
      sub3CategoryHTML += '<input type="radio" name="sub3Category" value="' + sub3Categories[i] + '">' + sub3Categories[i] + '';
    }
    $('#sub3Category').html(sub3CategoryHTML); // サブサブカテゴリが表示されたときに、変数の中身をHTMLとして追加する
    $('#itemDetails-2').html(''); // サブサブカテゴリが表示されたときに、アイテム詳細をリセット
  }

  function showSizeOptions(sizes) {
    var sizeHTML = '';
    for (var i = 0; i < sizes.length; i++) {
      sizeHTML += '<input type="radio" name="size" value="' + sizes[i] + '">' + sizes[i] + ' ';
    }
    $('#itemDetails-2').html(sizeHTML);
  }
});
