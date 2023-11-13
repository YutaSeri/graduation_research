function validateForm() {
    var input = document.getElementById('q').value;
    if (input.trim() === '') {
      // もし入力が空だった場合、アラートを表示してフォームの送信をキャンセル
      alert('名前を入力してください');
      return false;
    }
    // 入力がある場合はフォームを送信
    return true;
  }