

    // Открыть модальное окно
    function openModal() {
      var modal = document.getElementById("myModal");
      modal.style.display = "block";
    }

    // Закрыть модальное окно
    function closeModal() {
      var modal = document.getElementById("myModal");
      modal.style.display = "none";
    }

    // Подтвердить удаление
    function confirmDelete() {
      var deleteModal = document.getElementById("deleteModal");
      deleteModal.style.display = "block";
      return false; // Отменяем отправку формы по умолчанию
    }

    // Закрыть модальное окно удаления
    function closeDeleteModal() {
      var deleteModal = document.getElementById("deleteModal");
      deleteModal.style.display = "none";
    }

    // Удалить сотрудника
    function deleteEmployee() {
      // Выполните дополнительные действия перед удалением сотрудника (если необходимо)

      // Отправка запроса на сервер для удаления сотрудника
      var form = document.querySelector('.delete-form_contract');
      form.submit();
    }

    function addContract() {
      var contractNumber = document.getElementById("contractNumberInput").value;
      var date = document.getElementById("dateInput").value;
      var amount = document.getElementById("amountInput").value;
      var customer = document.getElementById("customerInput").value;
      var workType = document.getElementById("workTypeInput").value;
      var workTypeName = document.getElementById("workTypeNameInput").value;

      // Отправляем данные на серверную часть Flask
      $.ajax({
        url: "/add_contract",
        type: "POST",
        data: {
          contractNumber: contractNumber,
          date: date,
          amount: amount,
          customer: customer,
          workType: workType,
          workTypeName: workTypeName
        },
        success: function(response) {
          location.reload();
        },
      });
    }
