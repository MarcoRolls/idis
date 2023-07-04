
    function prepareDocuments() {
      var newDocumentsInput = document.getElementById('new-documents');
      var newDocuments = document.querySelectorAll('.new-document-card');
      var newDocumentsData = [];
      newDocuments.forEach(function(newDocument) {
        var type_documents = newDocument.querySelector('h3').textContent;
        var documentField = newDocument.querySelector('input[name="document"]');
        var documentValue = documentField.value;
        newDocumentsData.push({ type_documents: type_documents, document: documentValue  });
      });
      newDocumentsInput.value = JSON.stringify(newDocumentsData);


      var existingDocumentsInput = document.getElementById('existing-documents');
      var existingDocuments = document.querySelectorAll('.document-card:not(.new-document-card)');
      var existingDocumentsData = [];
      existingDocuments.forEach(function(existingDocument) {
        var type_documents = existingDocument.querySelector('h3').textContent;
        var document = existingDocument.querySelector('img').src;
        existingDocumentsData.push({ type_documents: type_documents, document: document });
      });
      existingDocumentsInput.value = JSON.stringify(existingDocumentsData);
    }

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
      var form = document.querySelector('.delete-form_user');
      form.submit();
    }

    function addEmployee() {
      var surname = document.getElementById("surnameInput").value;
      var name = document.getElementById("nameInput").value;
      var telephone = document.getElementById("telephoneInput").value;
      var mail = document.getElementById("mailInput").value;

      // Отправляем данные на серверную часть Flask
      $.ajax({
        url: "/add_employee",
        type: "POST",
        data: {
          surname: surname,
          name: name,
          telephone: telephone,
          mail: mail
        },
        success: function(response) {
          location.reload();
        },
      });
    }


////////////////////


    function uploadDocument() {
      var typeDocumentsInput = document.getElementById('type_documents');
      var documentInput = document.getElementById('document');

      // Создание карточки документа
      var card = document.createElement('div');
      card.classList.add('document-card', 'new-document-card');

      var h3 = document.createElement('h3');
      h3.textContent = typeDocumentsInput.value;
      card.appendChild(h3);

      var img = document.createElement('img');
      img.src = URL.createObjectURL(documentInput.files[0]);
      img.alt = 'Документ';
      card.appendChild(img);


      var deleteForm = document.createElement('form');
      deleteForm.classList.add('delete-form');

      var typeDocumentsInputHidden = document.createElement('input');
      typeDocumentsInputHidden.type = 'hidden';
      typeDocumentsInputHidden.name = 'type_documents';
      typeDocumentsInputHidden.value = typeDocumentsInput.value;
      deleteForm.appendChild(typeDocumentsInputHidden);

      var documentInputHidden = document.createElement('input');
      documentInputHidden.type = 'hidden';
      documentInputHidden.name = 'document';
      // Преобразование файла в формат base64
      var reader = new FileReader();
      reader.onload = function(event) {
        documentInputHidden.value = event.target.result;
      };
      reader.readAsDataURL(documentInput.files[0]);
      deleteForm.appendChild(documentInputHidden);

      var deleteButton = document.createElement('button');
      deleteButton.type = 'button';
      deleteButton.classList.add('delete-button');
      deleteButton.textContent = 'Удалить';
      deleteButton.addEventListener('click', function() {
        card.remove(); // Удаление карточки документа из DOM
      });
      deleteForm.appendChild(deleteButton);

      card.appendChild(deleteForm);

      var newDocumentsContainer = document.getElementById('new-documents-container');
      newDocumentsContainer.appendChild(card);


      // Сброс полей формы
      typeDocumentsInput.value = '';
      documentInput.value = '';
    }

    var uploadForm = document.getElementById('uploadForm');
    uploadForm.addEventListener('submit', function(event) {
      event.preventDefault();
      uploadDocument();
      closeModal();
    });

    // Функция для удаления существующего документа
    function deleteExistingDocument(button) {
      var card = button.parentElement.parentElement;
      card.remove(); // Удаление карточки документа из DOM
    }