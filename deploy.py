#!/bin/bash

# 사용자에게 커밋 메시지 입력 받기
read -p "커밋 메시지를 입력하세요: " USER_MSG

# 현재 날짜와 시간
DATE=$(date "+%Y-%m-%d_%H:%M")

# 최종 커밋 메시지 생성
COMMIT_MSG="${DATE}_${USER_MSG}"

# Git 명령어 실행
git add .
git commit -m "$COMMIT_MSG"
git push
