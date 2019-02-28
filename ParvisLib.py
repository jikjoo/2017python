import sqlite3

conn = sqlite3.connect("..\database\parvislib.db")
with conn :
    class MainWord:
        # 메인워드 클래스  .word = 입력받은 단어 모음 .main_word  .meaning  .main_id
        def __init__(self, word=['']):
            self.word = tuple(word)
            cur = conn.cursor()
            main_list = []
            meaning_list = []
            id_list = []
            for w in self.word:
                cur.execute("SELECT * FROM main WHERE main_word = ?",[w])
                result = cur.fetchall()
                m_list = []
                n_list = []
                for r in result :
                    n_list.append(r[0])
                    m_list.append(r[2])
                if result :
                    main_list.append(w)
                    meaning_list.append(m_list)
                    id_list.append(n_list)
                    

            self.main_word = tuple(main_list)   #DB에 있는 단어
            self.meaning = tuple(meaning_list)  #뜻
            self.main_id = tuple(id_list)       #id


        #새로운 메인워드 추가
        def insert(self):
            for w in self.word:
                cur = conn.cursor()
                cur.execute("INSERT INTO main (main_word) VALUES (?)",[w])
                conn.commit()
        
        #새로운 뜻 추가
        def update(self, meaning=['']):
            query = "UPDATE main SET meaning = ? WHERE main_id = ? AND meaning IS NULL"
            if len(self.word) == len(meaning) :
                s = self.main_word
                i = 0
                for w in self.word:
                    if  s.count(w) :# 문자가 DB 있으면
                        j = 0
                        for id0 in self.main_id[i] :
                            if not self.meaning[i][j] :
                                cur = conn.cursor()
                                cur.execute(query, (meaning[i], id0))
                                conn.commit()
                                break
                            j += 1
                    else :
                        cur = conn.cursor()
                        cur.execute("INSERT INTO main (main_word, meaning) VALUES (?,?)", (w,meaning[i]))
                        conn.commit()
                    i += 1
            else :
                print("error : main_word 수랑 meaning 수랑 맞지 않음")

        # 테이블에 존재하는 메인워드들의 튜플

        #main_id 선택
        def choice(self):
            pass

with conn:
    class MainID:
        #메인아이디 클래스
        def __init__(self, main_id):
            self.main_id = main_id
            cur = conn.cursor()
            cur.execute("SELECT * FROM main WHERE main_id = ?", (self.main_id,))
            result_main = cur.fetchall()
            cur = conn.cursor()
            cur.execute("SELECT sub_word FROM sub WHERE main_id = ?", (self.main_id,))
            result_sub = cur.fetchall()
            subs = []
            for r in result_sub :
                subs.append(r[0])
            self.main_word = result_main[0][1]  # DB에 있는 단어
            self.meaning = result_main[0][2]  # 뜻
            self.sub_words = subs      #서브 워드들
        #서브워드 추가
        def insert_sub(self, subs = ['']):
            query = "INSERT INTO sub (main_id, sub_word) VALUES (?,?)"
            for sub in subs :
                cur = conn.cursor()
                cur.execute(query,(self.main_id, sub))
                conn.commit()

        def insert_foreign(self, subs=['']):
            query = "INSERT INTO sub (main_id, sub_word, category) VALUES (?,?,'번역어')"
            for sub in subs :
                cur = conn.cursor()
                cur.execute(query,(self.main_id, sub))
                conn.commit()

    #입력 보조 함수
    def input_helper() :
        inp_list = []
        i =0
        while True:
            print(i,"번 입력")
            inp = input()
            i+=1
            if not inp :break
            inp_list.append(inp)
        return inp_list

     #테스트용

    def test_lib():
        print("옵션:"
              "\n1: insert main word list"
              "\n2: search main word"
              "\n3: update meaning"
              "\n4: search main id"
              "\n5: insert sub word")
        opt = input()

        if(opt == '1') :                    #메인단어 추가
            print("메인 단어 리스트 : ")
            inp_list = input_helper()
            print(inp_list)
            test = MainWord(inp_list)
            test.insert()
        elif opt == '2' :                 #메인단어 검색
            print("검색할 메인단어")
            inp_list = input_helper()
            test = MainWord(inp_list)
            print("검색된 메인 단어 : ", test.main_word)
            print("검색된 뜻 : ", test.meaning)
            print("검색된 id : ", test.main_id)
        elif(opt=='3'):                       #메인단어랑 뜻 추가
            print("메인단어 리스트")
            inp_list = input_helper()
            print("뜻 리스트")
            mean_list = input_helper()

            test = MainWord(inp_list)
            test.update(mean_list)
        elif opt == '4' :
            print("메인 아이디 : ")
            inp = input()
            test = MainID(inp)
            print("검색된 메인 아이디 : ",test.main_id)
            print("검색된 메인 단어 : ", test.main_word)
            print("검색된 뜻 : ", test.meaning)
            print("검색된 유의어 : ",test.sub_words)
        elif opt == '5':
            print("메인 단어 : ")
            inp = input_helper()
            test=MainWord(inp)
            print("메인 아이디 선택 : ", test.main_id)
            while True :
                sel = int(input())
                if sel > len(test.meaning) :
                    print("다시 선택")
                else :
                    id0 = test.main_id[0][sel]
                    break
            print("서브 단어 입력 : ")
            subs = input_helper()
            test_sub = MainID(id0)
            test_sub.insert(subs)

        query = "SELECT main.main_word,main.meaning,sub.sub_word FROM main" \
                " LEFT OUTER JOIN sub ON main.main_id = sub.main_id"
        cur = conn.cursor()
        cur.execute(query)
        items_list = cur.fetchall()



        for it in items_list:
            print(it)

    if __name__ == "__main__":
        test_lib()