  $(document).ready(function() {
    $(".sub-radio").hide();

    $("[name='medical-items']").click(function() {
      $(".sub-radio").hide(); // すべてのサブ項目を非表示にする
      if ($(this).is(":checked")) {
          // 選択したラジオボタンのサブ項目のみを表示する
          $(this).siblings(".sub-radio").show();
      }
    });

    $("[name='dietary-items']").click(function() {
      $(".sub-radio").hide(); // すべてのサブ項目を非表示にする
      if ($(this).is(":checked")) {
          // 選択したラジオボタンのサブ項目のみを表示する
          $(this).siblings(".sub-radio").show();
      }
    });

    $("[name='baby-items']").click(function() {
      $(".sub-radio").hide(); // すべてのサブ項目を非表示にする
      if ($(this).is(":checked")) {
          // 選択したラジオボタンのサブ項目のみを表示する
          $(this).siblings(".sub-radio").show();
      }
    });
   
    $("[name='psychological-items']").click(function() {
      $(".sub-radio").hide(); // すべてのサブ項目を非表示にする
      if ($(this).is(":checked")) {
          // 選択したラジオボタンのサブ項目のみを表示する
          $(this).siblings(".sub-radio").show();
      }
    });

    $("[name='learning-items']").click(function() {
      $(".sub-radio").hide(); // すべてのサブ項目を非表示にする
      if ($(this).is(":checked")) {
          // 選択したラジオボタンのサブ項目のみを表示する
          $(this).siblings(".sub-radio").show();
      }
    });

    $("[name='clothing-items']").click(function() {
      $(".sub-radio").hide(); // すべてのサブ項目を非表示にする
      if ($(this).is(":checked")) {
          // 選択したラジオボタンのサブ項目のみを表示する
          $(this).siblings(".sub-radio").show();
      }
    });
  

    // $("#radio1").click(function() {
        // $(".support-items .sub-radio").toggle();
    // });
     
    // $("#radio2").click(function() {
    //   $(".dietary-items .sub-radio").toggle();
    // });

    // $("#radio3").click(function() {
    //   $(".baby-items .sub-radio").toggle();
    // });

    // $("#radio4").click(function() {
    //   $(".psychological-items .sub-radio").toggle();
    // });

    // $("#radio5").click(function() {
    //   $(".learning-items .sub-radio").toggle();
    // });
    // $("#radio6").click(function() {
    //   $(".clothing-items .sub-radio").toggle();
    // });
});









  
