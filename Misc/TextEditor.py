def solution(queries):
    text_edit = TextEditor()
    result = []
    for query in queries:
        if query[0] == 'APPEND':
            result.append(text_edit.append(query[1]))
        elif query[0] == 'MOVE':
            result.append(text_edit.move(int(query[1])))
        elif query[0] == 'DELETE':
            result.append(text_edit.delete())
        elif query[0] == 'SELECT':
            result.append(text_edit.select(int(query[1]), int(query[2])))
        elif query[0] == 'COPY':
            result.append(text_edit.copy_op())
        elif query[0] == 'PASTE':
            result.append(text_edit.paste())
        elif query[0] == 'UNDO':
            result.append(text_edit.undo_op())
        elif query[0] == 'REDO':
            result.append(text_edit.redo_op())
    return result


class TextEditor(object):
    def __init__(self):
        self.undo = []
        self.redo = []
        self.text = ''
        self.cur = 0
        self.left_cur = 0
        self.right_cur = 0
        self.selected = ""
        self.copied_text = ""
        self.undo_flag = -1

    def append(self, words):
        self.undo_flag = -1
        self.redo = []
        self.undo.append(["APPEND", self.text, self.cur])
        if len(self.selected) == 0:
            self.text = self.text[:self.cur] + words + self.text[self.cur:]
            self.cur = self.cur + len(words)
        else:
            self.text = self.text[:self.left_cur] + words + self.text[self.right_cur:]
            self.cur = self.left_cur + len(words)
        self.selected = ""
        return self.text

    def move(self, position):
        self.cur = position
        if self.cur >= len(self.text):  # >= ????
            self.cur = len(self.text)
        elif self.cur < 0:
            self.cur = 0
        print(self.cur)
        if len(self.selected) > 0:
            self.selected = ""
            self.left_cur = 0
            self.right_cur = 0
        return self.text

    def delete(self):
        self.undo_flag = -1
        self.redo = []

        self.undo.append(["DELETE", self.text, self.cur])
        if len(self.selected) == 0:
            self.text = self.text[:self.cur] + self.text[self.cur + 1:]
        else:
            self.text = self.text[:self.left_cur] + self.text[self.right_cur:]
            self.cur = self.left_cur
        self.selected = ""
        return self.text

    def select(self, start, end):
        self.selected = ''
        self.left_cur = max(0, start)
        self.right_cur = min(end, n)
        n = len(self.text)
        for i in range(max(0, start), min(end, n)):
            self.selected += self.text[i]
        print(self.selected, len(self.selected))
        return self.text

    def copy_op(self):
        self.copied_text = self.selected
        return self.text

    def paste(self):
        self.redo = []
        self.undo_flag = -1
        if len(self.selected) == 0:
            self.text = self.text[:self.cur] + self.copied_text + self.text[self.cur:]
            self.cur = self.cur + len(self.copied_text)
        else:
            self.text = self.text[:self.left_cur] + self.copied_text + self.text[self.right_cur:]
            self.cur = self.left_cur + len(self.copied_text)
        self.selected = ""
        return self.text

    def undo_op(self):
        if not self.undo: return self.text
        undo_opr = self.undo.pop()
        self.redo.append([undo_opr[0], self.text, self.cur])
        self.text = undo_opr[-2]
        self.cur = undo_opr[-1]
        self.undo_flag = 1
        return self.text

    def redo_op(self):
        if self.undo_flag == -1 or len(self.redo) == 0:
            self.redo = []
            return self.text
        redo_opr = self.redo.pop()
        self.text = redo_opr[-2]
        self.cur = redo_opr[-1]
        return self.text
