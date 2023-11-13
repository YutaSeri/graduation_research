var categories1 = {
  "医療・介護用品": ['松葉杖', '車椅子', '歩行器', '大人用おむつ'],
  "食料品": ['パン', 'カップめん', '水', 'ベビーフード'],
  "幼児用品": [ '紙おむつ', 'ミルク', 'ベビーベッド'],
  "その他": ['衣服品', '靴', 'トイレットペーパー', '毛布', '携帯トイレ',],
};
var categories2 = {
    "松葉杖": ['SS(121~137cm)', 'S(137~157cm)','M(157~178cm)','L(178~198cm)'],
    "車椅子": ['大型', '中型', '小型'],
    "歩行器": ['サークル型', '四輪歩行車'],
    "大人用おむつ": ['S', 'M','L'],
    "衣服品": ['上着', 'ズボン'],
    "靴": ['運動靴', '長靴'],
};
var categories3 = {
  "上着": ['長袖', '半袖'],
  "ズボン": ['長ズボン', '半ズボン'],
  "運動靴":['15cm','16cm','17cm','18cm','19cm','20cm','21cm','22cm','23cm','23.5cm','24cm','24.5cm','25cm','25.5cm','26cm','26.5cm','27cm','27.5cm','28cm','28.5cm','29cm','29.5cm','30cm'],
  "長靴":['15cm','16cm','17cm','18cm','19cm','20cm','21cm','22cm','23cm','23.5cm','24cm','24.5cm','25cm','25.5cm','26cm','26.5cm','27cm','27.5cm','28cm','28.5cm','29cm','29.5cm','30cm'],
};
var categories4 = {
  "長袖": ['120cm', '130cm', '140cm', '150cm', '160cm', 'XS', 'S', 'M', 'L', 'XL', '2XL', '3XL', '4XL'],
  "半袖":['120cm', '130cm', '140cm', '150cm', '160cm', 'XS', 'S', 'M', 'L', 'XL', '2XL', '3XL', '4XL'],
  "長ズボン":['120cm', '130cm', '140cm', '150cm', '160cm', 'XS', 'S', 'M', 'L', 'XL', '2XL', '3XL', '4XL'],
  "半ズボン":['120cm', '130cm', '140cm', '150cm', '160cm', 'XS', 'S', 'M', 'L', 'XL', '2XL', '3XL', '4XL'],
};

$(document).ready(function(){
  $("#category").change(function(){
    $("#category1").html('');
    $("#category2").html('');
    $("#category3").html('');
    $("#category4").html('');
    $("#category5").html('');
    $("#category6").html('');
    $("#label-1").html('');
    $("#label-2").html('').hide();
    $("#label-3").html('').hide();
    $("#label-4").html('').hide();
    $("#label-5").html('').hide();
    $("#label-6").html('').hide();

    var Category1 = $(this).val();
    var options = categories1[Category1];
    var selectElement = '<select id="category" class="form-control" name="category1">';
    if (Category1 === "テキスト入力") {
      $("#label-1").html('<label for="category">入力欄:</label>').show();
      $("#category1").html('<input type="text" class="form-control" name="category1">');
      $("#label-2").html('<label for="category">個数:</label>').show();
      $("#category2").html('<input type="number" name="quantity" min="1"><br><br><button class="btn btn-primary" type="submit">送信</button>');
    } else {
      selectElement += '<option hidden>項目を選択してください &#9660</option>';
      $("#label-1").html('<label for="category">項目2:</label>');
    } for(var i=0; i<options.length; i++){
        selectElement += '<option value="'+options[i]+'">'+options[i]+'</option>';
      }
      selectElement += '</select>';
      $("#category1").html(selectElement);

    $("#category1 select").change(function(){
      $("#category2").html('');
      $("#category3").html('');
      $("#category4").html('');
      $("#category5").html('');
      $("#category6").html('');
      $("#label-2").html('');
      $("#label-3").html('').hide();
      $("#label-4").html('').hide();
      $("#label-5").html('').hide();
      $("#label-6").html('').hide();

      var Category2 = $(this).val();
      var options2 = categories2[Category2];
      var selectElement2 = '<select id="category" class="form-control" name="category2">';
      if (options2 === undefined || options2.length === 0) {
        $("#label-2").html('<label for="category">備考欄:</label>').show();
        $("#category2").html('<input type="text" class="form-control" name="category2">');
        $("#label-3").html('<label for="category">個数:</label>').show();
        $("#category3").html('<input type="number" name="quantity" min="1"><br><br><button class="btn btn-primary" type="submit">送信</button>');
      } else {
        selectElement2 += '<option hidden>項目を選択してください &#9660</option>';
        $("#label-2").html('<label for="category">項目3:</label>').show();
      } for(var j=0; j<options2.length; j++){
        selectElement2 += '<option value="'+options2[j]+'">'+options2[j]+'</option>';
      }
      selectElement2 += '</select>';
      $("#category2").html(selectElement2);

      $("#category2 select").change(function(){
        $("#category3").html('');
        $("#category4").html('');
        $("#category5").html('');
        $("#category6").html('');
        $("#label-3").html('');
        $("#label-4").html('').hide();
        $("#label-5").html('').hide();
        $("#label-6").html('').hide();

        var Category3 = $(this).val();
        var options3 = categories3[Category3];
        var selectElement3 = '<select id="category" class="form-control" name="category3">';
        if (options3 === undefined || options3.length === 0) {
          $("#label-3").html('<label for="category">備考欄:</label>').show();
          $("#category3").html('<input type="text" class="form-control" name="category3">');
          $("#label-4").html('<label for="category">個数:</label>').show();
          $("#category4").html('<input type="number" name="quantity" min="1"><br><br><button class="btn btn-primary" type="submit">送信</button>');
        } else {
          selectElement3 += '<option hidden>項目を選択してください &#9660</option>';
          $("#label-3").html('<label for="category">項目4:</label>').show();
        } for(var j=0; j<options3.length; j++){
          selectElement3 += '<option value="'+options3[j]+'">'+options3[j]+'</option>';
        }
        selectElement3 += '</select>';
        $("#category3").html(selectElement3);

        $("#category3 select").change(function(){
          $("#category4").html('');
          $("#category5").html('');
          $("#category6").html('');
          $("#label-4").html('');
          $("#label-5").html('').hide();
          $("#label-6").html('').hide();
  
          var Category4 = $(this).val();
          var options4 = categories4[Category4];
          var selectElement4 = '<select id="category" class="form-control" name="category4">';
          if (options4 === undefined || options4.length === 0) {
            $("#label-4").html('<label for="category">備考欄:</label>').show();
            $("#category4").html('<input type="text" class="form-control" name="category4">');
            $("#label-5").html('<label for="category">個数:</label>').show();
            $("#category5").html('<input type="number" name="quantity" min="1"><br><br><button class="btn btn-primary" type="submit">送信</button>');
          } else {
            selectElement4 += '<option hidden>項目を選択してください &#9660</option>';
            $("#label-4").html('<label for="category">項目5:</label>').show();
          } for(var j=0; j<options4.length; j++){
            selectElement4 += '<option value="'+options4[j]+'">'+options4[j]+'</option>';
          }
          selectElement4 += '</select>';
          $("#category4").html(selectElement4);

          $("#category4 select").change(function(){
            $("#category5").html('');
            $("#category6").html('');
            $("#label-5").html('').hide();
            $("#label-6").html('').hide();
    
            var Category5 = $(this).val();
            var selectElement5 = '<select id="category" class="form-control" name="category5">';
            $("#label-5").html('<label for="category">備考欄:</label>').show();
            $("#category5").html('<input type="text" class="form-control" name="category5">');
            $("#label-6").html('<label for="category">個数:</label>').show();
            $("#category6").html('<input type="number" name="quantity" min="1"><br><br><button class="btn btn-primary" type="submit">送信</button>');
            $("#category5").html(selectElement5);
          });
        });
      });
    });
  });
});