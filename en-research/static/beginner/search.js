function validateForm() {
    var nameInput = document.getElementById('q').value;
    var birthdateInput = document.getElementById('birthdate').value;

    if (nameInput.trim() === '') {
        alert('名前を入力してください');
        return false;
    }

    if (birthdateInput.trim() === '') {
        alert('生年月日を入力してください');
        return false;
    }

    // 入力がある場合はフォームを送信
    return true;
}