#!/bin/bash

# 사용자에게 커밋 메시지를 입력 받기 (입력이 없으면 'UPDATED' 사용)
read -p "커밋 메시지를 입력하세요 (기본: UPDATED): " USER_MSG

# 입력이 비었을 경우 기본 메시지로 설정
if [ -z "$USER_MSG" ]; then
  USER_MSG="UPDATED"
fi

# 현재 날짜와 시간
DATE=$(date "+%Y-%m-%d %H:%M:%S")

# 최종 커밋 메시지
COMMIT_MSG="${USER_MSG} | ${DATE}"

# Git 명령어 실행
git add .
git commit -m "$COMMIT_MSG"
git push