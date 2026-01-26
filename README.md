# 데이터 분석 프로젝트

Python을 사용한 데이터 분석 프로젝트입니다.

## 프로젝트 초기 설정 방법

### 1. 저장소 클론

```bash
git clone <repository-url>
cd suo
```

### 2. 가상환경 생성 및 활성화

#### Windows
```bash
# 가상환경 생성
python -m venv venv

# 가상환경 활성화
venv\Scripts\activate
```

#### macOS/Linux
```bash
# 가상환경 생성
python3 -m venv venv

# 가상환경 활성화
source venv/bin/activate
```

### 3. 라이브러리 설치

가상환경이 활성화된 상태에서 다음 명령어를 실행합니다:

```bash
pip install -r requirements.txt
```

### 4. 프로젝트 실행

```bash
# Python 스크립트 실행
python study.py

# Streamlit 앱 실행 (해당되는 경우)
streamlit run <앱파일명>.py
```

## 가상환경 비활성화

작업을 마친 후 가상환경을 비활성화하려면:

```bash
deactivate
```

## 프로젝트 구조

```
suo/
├── data_analysis/      # 데이터 파일
├── study.py           # 메인 스크립트
├── requirements.txt   # 필요한 라이브러리 목록
└── README.md          # 프로젝트 설명
```

## 사용된 주요 라이브러리

- **pandas** - 데이터 분석 및 처리
- **numpy** - 수치 계산
- **streamlit** - 웹 애플리케이션 프레임워크
- **openpyxl** - Excel 파일 처리
